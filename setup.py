
from distutils.core import setup
setup(
    name="twocheckout",
    version='1.1.0',
    description="2Checkout Python SDK using API 6.0",
    author="2Checkout",
    author_email="support@2checkout.com",
    url="https://www.2checkout.com",
    packages=["twocheckout"],
    python_requires=">=3.5",
    install_requires=[
        'requests >= 2.28.1',
        'pyjwt >= 2.0.1'
    ]
)
