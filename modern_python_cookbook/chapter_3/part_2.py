import logging
import logging.config

#syslogging
#linux logs to /dev/log or pass a tuple ('ADDR', port) for a remote server
SYSLOG_ADDRESS = '/var/run/syslog'

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(name)s: %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'default',
            'address': SYSLOG_ADDRESS
        }
    },
    'root': {
        'handlers': ['syslog'],
        'level': 'INFO'
    }
})

log = logging.getLogger()
log.info('vianey <3')
