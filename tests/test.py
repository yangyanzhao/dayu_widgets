#!/usr/bin/env python3
from aiohttp import ClientSession
import asyncio
import logging
import json
import os
import sys
from pathlib import Path

from miservice import MiAccount, MiNAService, MiIOService, miio_command, miio_command_help

MISERVICE_VERSION = '2.0.1'


def usage():
    print("MiService %s - XiaoMi Cloud Service\n" % MISERVICE_VERSION)
    print("Usage: The following variables must be set:")
    print("           export MI_USER=<Username>")
    print("           export MI_PASS=<Password>")
    print("           export MI_DID=<Device ID|Name>\n")
    print(miio_command_help(prefix=sys.argv[0] + ' '))


async def main(args):
    try:
        async with ClientSession() as session:
            env = os.environ
            account = MiAccount(session, username=env.get('MI_USER'), password=env.get('MI_PASS'),
                                token_store=os.path.join(str(Path.home()), '.mi.token'))
            if args.startswith('mina'):
                service = MiNAService(account)
                result = await service.device_list()
                if len(args) > 4:
                    await service.send_message(result, -1, args[4:])
            else:
                service = MiIOService(account)
                result = await miio_command(service, env.get('MI_DID'), args, sys.argv[0] + ' ')
            if not isinstance(result, str):
                result = json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        result = e
    print(result)


if __name__ == '__main__':
    # 设置账号密码
    env = os.environ
    argv = sys.argv
    env.setdefault('MI_USER', '15267398131')
    env.setdefault('MI_PASS', '1324355181sllclz')
    env.setdefault('MI_DID', '423342314')  # 执行list命令可获取设备ID，执行list命令时，此选项可不填。
    # 执行命令
    argv.append('list')
    argc = len(argv)
    if argc > 1 and argv[1].startswith('-v'):
        argi = 2
        index = int(argv[1][2]) if len(argv[1]) > 2 else 4
        level = [logging.NOTSET, logging.FATAL, logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG][index]
    else:
        argi = 1
        level = logging.WARNING
    if argc > argi:
        if level != logging.NOTSET:
            _LOGGER = logging.getLogger('miservice')
            _LOGGER.setLevel(level)
            _LOGGER.addHandler(logging.StreamHandler())
        asyncio.run(main(' '.join(argv[argi:])))
    else:
        usage()
