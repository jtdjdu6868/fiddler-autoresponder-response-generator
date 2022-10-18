# fiddler-autoresponder-response-generator
Generates http response file for Fiddler AutoResponder  
  
Make this program is because there is need to fill content length and mimetype in to http header when making response file for Fiddler everytime.  
Obviously those steps can be done by automatic program.

## Usage
`frg.py CONTENT_FILE_NAME OUTPUT_FILE_NAME [FORCE_MIMETYPE]`  
* Basic mimetype table is included, but if your file type was not in that table, or you want to force a mimetype, you can call with adding force mimetype.  
* if your file type was not in mimetype table and you havn't add a mimetype param, default mimetype is `text/plain`.
