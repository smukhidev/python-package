# shurjopay Integration Library 
Shurjopay integration Library 

###How to use it aka Quickstart

1. Install: 
    
   ``` 
    pip install shurjopay-pkg-tareq
    ```
   To install Python package from github, you need to clone that repository.
   
   ```
   git clone https://github.com/tareqanam/surjopay.git
   ```
   
   Then just run the setup.py file from that directory,
   
   ```
   sudo python setup.py install
   ```
    
2. Import shurjoPay class:

    ```
    >>> from shurjopay import shurjoPay
    ```
3. Pass shurjoPay credential as parameters:
    
    ```
    >>> test = shurjoPay.ShurjoPay("merchant_name", "merchant_pass", "post_url", "decrypt_url", "merchant_prefix")
    ```
4. The following methods are available:

    4. **send_request**: The following parameters need to be passed:
        - *client_ip*: remote address of the client e.g. `103.0.0.1`
        - *transaction_id*: a unique id that starts with the given merchant prefix e.g. `"NOK"`
        - *amount*: amount
        - *return_url*: a return url that accepts `POST` method for encrypted `"spdata"` 
    4. **get_decrypt**: 
        The encrypted response data need to be passed.