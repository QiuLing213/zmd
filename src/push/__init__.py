import logging

from push.serverchan3 import push_serverchan3
from push.pushplus import push_pushplus
from push.qmsg import push_qmsg

__available_pusher = {
    'serverchan3': push_serverchan3,
    'pushplus': push_pushplus,
    'QMSG': push_qmsg,
}


def push(all_logs: list[str]):
    logging.info("开始推送结果")
    for k, v in __available_pusher.items():
        try:
            v(all_logs)
        except Exception as e:
            logging.error(f"[Push] {k}时出现问题", exc_info=e)
    logging.info("推送结束")
