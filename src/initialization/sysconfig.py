# coding=utf-8

import configparser


def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    cfg.read(cfg_file)
    return cfg

# 同读取文件，路径和视频不一样
sys_cfg = read_config('../cfg/auto.cfg')

if __name__ == "__main__":
    cfg = read_config("../../cfg/auto.cfg")
    print(cfg.get('corp_para', 'corp_id'))
