#!/bin/bash
cd /workspace && uvicorn app.core.main:app --reload --port=8080 --host=0.0.0.0