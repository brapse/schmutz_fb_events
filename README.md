Schmutz Facebook Event Extraction
=================================
Pull the details about facebook events from the graph API. 

# Installation
```
make install
```

Takes a file with facebook event, one per line and outputs a csv of
event details.

For instance, let `input.txt` be a regular text file with the contents:
```
https://www.facebook.com/events/1220567301376538/
https://www.facebook.com/events/1964014003867518/
https://www.facebook.com/events/136865533602812/
```

and `$SCHMUTZ_ACCESS_TOKEN` be a Facebook API access token.

Then running:
```
python schmutz_fb_events/cli.py --access-token=$SCHMUTZ_ACCESS_TOKEN input.txt
```

Will produce:
```
```
