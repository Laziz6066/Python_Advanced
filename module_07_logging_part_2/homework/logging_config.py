LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'debug_formatter': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        },
        'error_formatter': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'filters': {
        'ascii_filter': {
            '()': 'app.ASCIIFilter'
        }
    },
    'handlers': {
        'debug_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'debug_formatter',
            'filters': ['ascii_filter'],
            'filename': 'calc_debug.log'
        },
        'error_handler': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'error_formatter',
            'filters': ['ascii_filter'],
            'filename': 'calc_error.log'
        },
        'flask_handler': {
            'class': 'path.to.FlaskHandler',  # Replace 'path.to' with the actual path to FlaskHandler
            'level': 'DEBUG',
            'formatter': 'debug_formatter',
            'url': 'http://localhost:5000/logs'  # Replace with the actual URL of your Flask server
        }
    },
    'loggers': {
        'app_log': {
            'handlers': ['debug_handler', 'error_handler', 'flask_handler'],
            'level': 'DEBUG'
        }
    }
}
