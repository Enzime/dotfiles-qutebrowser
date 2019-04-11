try:
    MODES = ('caret', 'command', 'hint', 'insert', 'normal', 'passthrough',
                'prompt', 'yesno')

    ENTER_KEYSYMS = ('<return>', '<shift-return>', '<enter>', '<shift-enter>')


    def config_bind_iter(iterable, *args, **kwargs):
        for binding in iterable:
            print(binding, args, kwargs)
            config.bind(binding, *args, **kwargs)

    c.bindings.default = {}

    for mode in MODES:
        if mode == 'normal':
            config.bind('<escape>',
                            'clear-keychain ;; search ;; fullscreen --leave',
                            mode='normal')
        elif mode == 'passthrough':
            config.bind('<ctrl-[>', 'leave-mode', mode=mode)
        else:
            config.bind('<escape>', 'leave-mode', mode=mode)

    config.bind(':', 'set-cmd-text :', mode='normal')
    config.bind('i', 'enter-mode insert', mode='normal')
    config.bind('/', 'set-cmd-text /', mode='normal')
    config.bind('?', 'set-cmd-text ?', mode='normal')
    config.bind('<ctrl-v>', 'enter-mode passthrough', mode='normal')

    config.bind('ZQ', 'quit', mode='normal')
    config.bind('ZR', 'restart', mode='normal')

    config.bind('d', 'tab-close', mode='normal')
    config.bind('D', 'tab-close -o', mode='normal')
    config.bind('r', 'reload', mode='normal')
    config.bind('R', 'reload -f', mode='normal')
    config.bind('u', 'undo', mode='normal')

    config.bind('co', 'set-cmd-text -s :open', mode='normal')
    config.bind('cc', 'set-cmd-text :open {url}', mode='normal')
    config.bind('to', 'set-cmd-text -s :open -t', mode='normal')
    config.bind('tc', 'set-cmd-text :open -t {url}', mode='normal')
    config.bind('wo', 'set-cmd-text -s :open -w', mode='normal')
    config.bind('wc', 'set-cmd-text :open -w {url}', mode='normal')

    config.bind('b', 'set-cmd-text -s --run-on-count :buffer', mode='normal')

    config_bind_iter(('h', '<left>'), 'scroll left', mode='normal')
    config_bind_iter(('j', '<down>'), 'scroll down', mode='normal')
    config_bind_iter(('k', '<up>'), 'scroll up', mode='normal')
    config_bind_iter(('l', '<right>'), 'scroll right', mode='normal')

    config.bind('gg', 'scroll-to-perc 0', mode='normal')
    config.bind('G', 'scroll-to-perc', mode='normal')

    config_bind_iter(('<ctrl-u>', '<pgup>'), 'scroll-page 0 -0.5', mode='normal')
    config_bind_iter(('<ctrl-d>', '<pgdown>'), 'scroll-page 0 0.5', mode='normal')

    config.bind('-', 'zoom-out', mode='normal')
    config.bind('+', 'zoom-in', mode='normal')
    config.bind('=', 'zoom', mode='normal')

    config.bind('n', 'search-next', mode='normal')
    config.bind('N', 'search-prev', mode='normal')

    config.bind('A', 'back', mode='normal')
    config.bind('tA', 'back -t', mode='normal')
    config.bind('F', 'forward', mode='normal')
    config.bind('tF', 'forward -t', mode='normal')

    config.bind('H', 'tab-move -', mode='normal')
    config.bind('J', 'tab-next', mode='normal')
    config.bind('K', 'tab-prev', mode='normal')
    config.bind('L', 'tab-move +', mode='normal')

    config.bind('y', 'yank', mode='normal')
    config.bind('Y', 'yank selection', mode='normal')

    config.bind('cp', 'open -- {clipboard}', mode='normal')
    config.bind('tp', 'open -t -- {clipboard}', mode='normal')
    config.bind('wp', 'open -w -- {clipboard}', mode='normal')

    config.bind('cC', 'tab-clone', mode='normal')

    config.bind('f', 'hint --rapid', mode='normal')
    config.bind('S', 'hint --rapid all tab', mode='normal')

    config.bind(';yi', 'hint images yank', mode='normal')
    config.bind(';yl', 'hint links yank', mode='normal')
    config.bind(';yri', 'hint --rapid images yank', mode='normal')
    config.bind(';yrl', 'hint --rapid links yank', mode='normal')

    config.bind(',do', 'download-open', mode='normal')
    config.bind(',dc', 'download-clear', mode='normal')
    config.bind(',dC', 'download-cancel', mode='normal')
    config.bind(',D', 'download', mode='normal')

    # config.bind('<ctrl-w>', 'fake-key <ctrl-backspace>', mode='insert')
    # config.bind('<ctrl-w>', 'rl-backward-kill-word', mode='command')
    # config.bind('<ctrl-w>', 'rl-backward-kill-word', mode='prompt')

    config.bind('<up>', 'command-history-prev', mode='command')
    config.bind('<down>', 'command-history-next', mode='command')

    config.bind('<tab>', 'completion-item-focus next', mode='command')
    config.bind('<shift-tab>', 'completion-item-focus prev', mode='command')
    config.bind('<shift-del>', 'completion-item-del', mode='command')
    config_bind_iter(ENTER_KEYSYMS, 'command-accept', mode='command')

    config_bind_iter(ENTER_KEYSYMS, 'prompt-accept', mode='prompt')

    config.bind('y', 'prompt-accept yes', mode='yesno')
    config.bind('n', 'prompt-accept no', mode='yesno')

    config.bind('cd', 'tab-give', mode='normal')
    config.bind('ca', 'set-cmd-text -s :tab-give', mode='normal')
    config.bind('tt', 'set-cmd-text -s :tab-take', mode='normal')

    c.auto_save.session = True

    c.backend = 'webengine'

    c.completion.quick = False

    c.downloads.location.directory = '/data/Downloads/'
    c.downloads.location.prompt = False
    c.downloads.open_dispatcher = 'rifle'

    c.input.forward_unbound_keys = 'none'

    c.tabs.background = True
    c.tabs.last_close = 'blank'
    c.tabs.show = 'always'

    c.url.default_page = 'about:blank'

    c.url.searchengines = {
        'DEFAULT': 'https://encrypted.google.com/search?q={}',
        '!g': 'https://encrypted.google.com/search?q={}',
        '!gi': 'https://encrypted.google.com/search?q={}&tbm=isch',
        '!gm': 'https://www.google.com/maps/search/{}/',
        '!yt': 'https://www.youtube.com/results?search_query={}',
        '!fb': 'https://www.facebook.com/search/top?q={}',
        '!btn': 'https://broadcasthe.net/series.php?name={}',
        '!nyaa': 'https://nyaa.si/?q={}',
        '!mal': 'https://myanimelist.net/search/all?q={}',
        '!gh': 'https://github.com/search?q={}',
        '!nix': 'https://search.nix.gsc.io/?q={}&i=nope&files=&repos=',
    }

    c.url.start_pages = ['about:blank']
except:
    import traceback; traceback.print_exc()
    import ipdb; ipdb.set_trace()
