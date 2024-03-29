FROM python:3.12-alpine AS builder

RUN apk add --no-cache curl

ENV PDM_HOME=/opt/pdm
RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 -

WORKDIR /opt/app
COPY pyproject.toml pdm.lock .
COPY src/ src/

RUN $PDM_HOME/bin/pdm sync --no-editable --production


FROM python:3.12-alpine

COPY --from=builder /opt/app /opt/app

ENV LITESTAR_APP=app.app:create_app

CMD ["/opt/app/.venv/bin/litestar", "run", "--port=$SERVER_PORT", "--host=$SERVER_HOST"]
