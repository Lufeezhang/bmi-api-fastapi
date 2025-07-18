#!/bin/bash
uvicorn main:bmi_api --host 0.0.0.0 --port $PORT
