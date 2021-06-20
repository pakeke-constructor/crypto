

### Sending to ledger:

This usually requires a public key private key pair.
The public key is usually the "account number".


Using basic cryptography:
```c
Sign(Message, <priv_key>)  ->   Signature

CheckValid(Message, Signature, <public_key>)  ->  True/False
```


This way, users can make transactions from their account that can be validated
easily. 

