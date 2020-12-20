class ArmaClassParserError(Exception):
    pass


class ContentFilterNoneError(ArmaClassParserError):
    def __init__(self, cfg_name, next_cfg_name):
        msg = f'filtered_raw_content is None after filtering sub-cfg: "{cfg_name}", next sub-cfg: "{next_cfg_name}"'
        super().__init__(msg)
