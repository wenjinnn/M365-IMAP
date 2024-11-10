import os
ClientId = "347227d5-402d-47b5-bcfe-ef427563b99e"
ClientSecret = ""
Scopes = ['https://outlook.office.com/IMAP.AccessAsUser.All','https://outlook.office.com/SMTP.Send']
RefreshTokenFileName = os.path.expanduser('~') + "/.cache/neomutt/imap_smtp_refresh_token"
AccessTokenFileName = os.path.expanduser('~') + "/.cache/neomutt/imap_smtp_access_token"

# Optionally specify a tenantId here: "https://login.microsoftonline.com/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/"
Authority = None 
