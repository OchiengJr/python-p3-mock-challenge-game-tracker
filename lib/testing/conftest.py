def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    
    # Handle cases where either pref or suf is None
    if pref is None:
        pref = ""
    if suf is None:
        suf = ""

    if pref or suf:
        item._nodeid = ' '.join((pref, suf)),
