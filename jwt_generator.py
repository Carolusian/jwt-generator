
# coding: utf-8

# In[4]:





# In[1]:


import python_jwt as jwt, jwcrypto.jwk as jwk, datetime
key = jwk.JWK.generate(kty='RSA', size=2048)
priv_pem = key.export_to_pem(private_key=True, password=None)
pub_pem = key.export_to_pem()
payload = { 'foo': 'bar', 'wup': 90 };
priv_key = jwk.JWK.from_pem(priv_pem)
pub_key = jwk.JWK.from_pem(pub_pem)
token = jwt.generate_jwt(payload, priv_key, 'RS256', datetime.timedelta(minutes=5))
header, claims = jwt.verify_jwt(token, pub_key, ['RS256'])
for k in payload: assert claims[k] == payload[k]
    
print priv_pem.decode()
print '---'
print pub_pem.decode()

