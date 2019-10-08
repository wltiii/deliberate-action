from threading import Timer
from threading import Event
from datetime import datetime, timezone

# from Thread import Timer

def do_my_thing():
    print(f'In {datetime.now(timezone.utc)}')
    print('hello, world')
    print(f'Out {datetime.now(timezone.utc)}')

exit = Event()

def main():
    print(f'Before {datetime.now(timezone.utc)}')
    while not exit.is_set():
      do_my_thing()
      exit.wait(30.0)
      exit.set()

    print('')
    print('All done!')
    exit.clear()
    # perform any cleanup here

def quit(signo, _frame):
    # print('Interrupted by %d, shutting down' % signo)
    exit.set()

if __name__ == '__main__':

    import signal
    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit)

    main()
