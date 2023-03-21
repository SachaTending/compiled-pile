import sys
log_prefix = "[INFO] Bootstrap:"
def log(*arg):
    print(log_prefix, " ".join(arg), file=sys.stderr)

target_libs = ['flask', 'loguru', 'loguru_logging_intercept']

missing = []

def bootstrap():
    import os
    log("Searching for target modules...")
    for i in target_libs:
        try: 
            __import__(i)
            del sys.modules[i]
        except: missing.append(i)
    log(f"Missing modules: {', '.join(missing)}")
    if missing != []:
        log("Installing...")
        import pip
        pip_argv = ['install']
        for i in missing:
            pip_argv.append(i)
        pip.main(pip_argv)
    log("Starting...")

bootstrap()