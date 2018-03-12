import click
import facebook
import re
import sys
import unicodecsv as csv

event_id_re = "events\/(\d+)"
expected_line_foramt = 'https://www.facebook.com/events/<event_id>>'

def format_field(input_str):
    return "'%s'" % input_str

@click.command()
@click.argument('input', required=True, type=click.Path(exists=True), nargs=1)
@click.option('--access-token', required=True, help='FacebookAPI Access token')
def run(input, access_token):
    """Scrape event details from facebook API"""

    with open(input, 'r') as f:
        for line in f:
            match = re.search(event_id_re, line)
            if not match:
                error = ("Line format error, expecting: %s \n got %s \n" % (expected_line_foramt, line))
                sys.stderr.write(error)
                continue

            event_id = match.group(1)

            graph = facebook.GraphAPI(access_token=access_token, version="2.7")
            event = graph.get_object(id=event_id)
            line = {'name': format_field(event['name']),
                    'band_names': format_field(event['name']),
                    'venue': format_field(event['place']['name']),
                    'door_time': format_field(event['start_time']),
                    'concert_time': format_field(event['start_time'])} # XXX: Is this the right assumption?

            output = ','.join([line['name'], line['band_names'], line['venue'], line['door_time'], line['concert_time']])

            print(output)

if __name__ == '__main__':
    run()
