#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_rule_engine

if __name__ == '__main__':
    result = apis.aep_rule_engine.saasCreateRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.saasQueryRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '10015488')
    print('result='+str(result))

    result = apis.aep_rule_engine.saasUpdateRule('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

    result = apis.aep_rule_engine.saasDeleteRuleEngine('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

