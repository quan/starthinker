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

'''
--------------------------------------------------------------

Before running this Airflow module...

  Install StarThinker in cloud composer from open source:

    pip install git+https://github.com/google/starthinker

  Or push local code to the cloud composer plugins directory:

    source install/deploy.sh
    4) Composer Menu
    l) Install All

--------------------------------------------------------------

CM Campaign Auditor

A tool for rapidly bulk checking Campaign Manager campaigns

Add this card to a recipe and save it.
Then click <strong>Run Now</strong> to deploy.
Follow the <a href="https://docs.google.com/spreadsheets/d/1tt597dMsAaxYXaJdifwKYNVzJrIl6E9Pe8GysfVrWOs/">instructions</a> for setup.

'''

from starthinker_airflow.factory import DAG_Factory

# Add the following credentials to your Airflow configuration.
USER_CONN_ID = "starthinker_user" # The connection to use for user authentication.
GCP_CONN_ID = "starthinker_service" # The connection to use for service authentication.

INPUTS = {
  'recipe_name': '',  # Name of document to deploy to.
}

TASKS = [
  {
    'drive': {
      'hour': [
      ],
      'copy': {
        'destination': {
          'field': {
            'description': 'Name of document to deploy to.',
            'prefix': 'CM User Editor For ',
            'order': 1,
            'kind': 'string',
            'name': 'recipe_name',
            'default': ''
          }
        },
        'source': 'https://docs.google.com/spreadsheets/d/1tt597dMsAaxYXaJdifwKYNVzJrIl6E9Pe8GysfVrWOs/'
      },
      'auth': 'user'
    }
  }
]

DAG_FACTORY = DAG_Factory('cm_campaign_audit', { 'tasks':TASKS }, INPUTS)
DAG_FACTORY.apply_credentails(USER_CONN_ID, GCP_CONN_ID)
DAG = DAG_FACTORY.execute()

if __name__ == "__main__":
  DAG_FACTORY.print_commandline()
