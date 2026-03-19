# Lower and upper threshold values for alarms
# This is used in the OPA alarm services

{   # 'users shift' regime
    'users': {
        'li': {
            'KlyArea':    [19.0, 22.0],  #[C]
            'KlyTemp':    [17.0, 22.0],  #[C]
            'Tunnel':     [22.0, 24.0],  #[C]
            'Umid':       [41.0, 53.0],  #[C]
            '45C':        [42.0, 46.0],  #[C]
            'Solenoid':   [23.0, 27.0],  #[C]
            },
        'tb': {
            'Septum':     [22.0, 26.0],  #[C]
            'Dipolo':     [22.0, 26.0],  #[C]
            'Board':      [38.0, 42.0],  #[C]
            },
        'ts': {
            'Septts01':   [22.0, 27.0],  #[C]
            'SeptEje':    [23.0, 27.0],  #[C]
            'Septts04':   [22.0, 26.0],  #[C]
            'Septts04b':  [22.0, 26.0],  #[C]
            },
        'bo': {
            'Group01_05': [20.0, 26.5],  #[C]
            'Group06_10': [20.0, 26.0],  #[C]
            'Group11_15': [20.0, 26.0],  #[C]
            'Group16_20': [20.0, 26.0],  #[C]
            'Group21_25': [20.0, 26.0],  #[C]
            'Group26_30': [20.0, 26.0],  #[C]
            'Group31_35': [20.0, 26.0],  #[C]
            'Group36_40': [20.0, 26.0],  #[C]
            'Group41_45': [20.0, 26.0],  #[C]
            'Group46_50': [20.0, 26.0],  #[C]
            },
        },
}
