# Container validation with Goss and Github Actions

This is a demo Flask app to try container validation with Goss and Github Actions.

## What is Goss

[Goss](https://github.com/aelsabbahy/goss) is a server testing/validation tool written in Go.

These are some of the tests used on this demo:

```yaml
package:
  py3-pip:
    installed: true
  python3:
    installed: true
port:
  tcp:5000:
    listening: true
    ip:
    - 0.0.0.0
http:
  http://127.0.0.1:5000:
    status: 200
    body:
    - Hello, World!
```

## Using Goss on Github Actions

To execute Goss tests use the [install-goss](https://github.com/marketplace/actions/install-goss) action from the marketplace. Then all you need to do is execute the `dgoss` script to validate the image.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Build Docker image
        run: docker build . -t test-example:dev

      - name: Install Goss
        uses: e1himself/goss-installation-action@v1.0.3

      - name: Execute Goss tests
        run: dgoss run test-example:dev
```
