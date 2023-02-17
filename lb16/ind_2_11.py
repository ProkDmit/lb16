#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def con(type: str):
    def act(nums: str):
        if type == 'list':
            return list(map(int, nums.split(' ')))
        if type == 'tuple':
            return tuple(map(int, nums.split(' ')))

    return act


if __name__ == "__main__":
    print(f"List: {con('list')('3 7 5 9 1')}")
    print(f"Tuple: {con('tuple')('5 7 1 3 6 8')}")
