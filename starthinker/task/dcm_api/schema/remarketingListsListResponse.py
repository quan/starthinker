###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

remarketingListsListResponse_Schema = [{
    'description': '',
    'name': 'kind',
    'type': 'STRING',
    'mode': 'NULLABLE'
}, {
    'description': '',
    'name': 'nextPageToken',
    'type': 'STRING',
    'mode': 'NULLABLE'
}, {
    'name':
        'remarketingLists',
    'type':
        'RECORD',
    'mode':
        'REPEATED',
    'fields': [
        {
            'description': '',
            'name': 'accountId',
            'type': 'INT64',
            'mode': 'NULLABLE'
        }, {
            'name': 'active',
            'type': 'BOOLEAN',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'advertiserId',
            'type': 'INT64',
            'mode': 'NULLABLE'
        },
        [{
            'description': '',
            'name': 'dimensionName',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'etag',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'id',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'kind',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': 'BEGINS_WITH, CONTAINS, EXACT, WILDCARD_EXPRESSION',
            'name': 'matchType',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'value',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }], {
            'description': '',
            'name': 'description',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'id',
            'type': 'INT64',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'kind',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'lifeSpan',
            'type': 'INT64',
            'mode': 'NULLABLE'
        },
        [{
            'description': '',
            'name': 'floodlightActivityId',
            'type': 'INT64',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'floodlightActivityName',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'name':
                'listPopulationClauses',
            'type':
                'RECORD',
            'mode':
                'REPEATED',
            'fields': [{
                'name':
                    'terms',
                'type':
                    'RECORD',
                'mode':
                    'REPEATED',
                'fields': [{
                    'name': 'contains',
                    'type': 'BOOLEAN',
                    'mode': 'NULLABLE'
                }, {
                    'name': 'negation',
                    'type': 'BOOLEAN',
                    'mode': 'NULLABLE'
                }, {
                    'description':
                        'NUM_EQUALS, NUM_GREATER_THAN, NUM_GREATER_THAN_EQUAL,'
                        ' NUM_LESS_THAN, NUM_LESS_THAN_EQUAL, STRING_CONTAINS,'
                        ' STRING_EQUALS',
                    'name':
                        'operator',
                    'type':
                        'STRING',
                    'mode':
                        'NULLABLE'
                }, {
                    'description': '',
                    'name': 'remarketingListId',
                    'type': 'INT64',
                    'mode': 'NULLABLE'
                }, {
                    'description':
                        'CUSTOM_VARIABLE_TERM, LIST_MEMBERSHIP_TERM, '
                        'REFERRER_TERM',
                    'name':
                        'type',
                    'type':
                        'STRING',
                    'mode':
                        'NULLABLE'
                }, {
                    'description': '',
                    'name': 'value',
                    'type': 'STRING',
                    'mode': 'NULLABLE'
                }, {
                    'description': '',
                    'name': 'variableFriendlyName',
                    'type': 'STRING',
                    'mode': 'NULLABLE'
                }, {
                    'description': '',
                    'name': 'variableName',
                    'type': 'STRING',
                    'mode': 'NULLABLE'
                }]
            }]
        }], {
            'description': '',
            'name': 'listSize',
            'type': 'INT64',
            'mode': 'NULLABLE'
        }, {
            'description':
                'REMARKETING_LIST_SOURCE_ADX, REMARKETING_LIST_SOURCE_DBM, '
                'REMARKETING_LIST_SOURCE_DFA, REMARKETING_LIST_SOURCE_DFP, '
                'REMARKETING_LIST_SOURCE_DMP, REMARKETING_LIST_SOURCE_GA, '
                'REMARKETING_LIST_SOURCE_GPLUS, REMARKETING_LIST_SOURCE_OTHER,'
                ' REMARKETING_LIST_SOURCE_PLAY_STORE, '
                'REMARKETING_LIST_SOURCE_XFP, REMARKETING_LIST_SOURCE_YOUTUBE',
            'name':
                'listSource',
            'type':
                'STRING',
            'mode':
                'NULLABLE'
        }, {
            'description': '',
            'name': 'name',
            'type': 'STRING',
            'mode': 'NULLABLE'
        }, {
            'description': '',
            'name': 'subaccountId',
            'type': 'INT64',
            'mode': 'NULLABLE'
        }
    ]
}]
