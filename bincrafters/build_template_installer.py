#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_shared


def get_builder(args=None, **kwargs):
    return build_shared.get_builder(args, **kwargs)
