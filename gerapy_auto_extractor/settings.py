import environs

env = environs.Env()
env.read_env()

APP_DEBUG = env.bool('APP_DEBUG', False)
