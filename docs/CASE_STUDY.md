# Lokesh Python Toolkit walkthrough

## Business problem

Small operational checks are hard to reuse when their inputs and tests are scattered. Each utility needs a documented command and an isolated fixture.

## Reproduce the workflow

Choose a utility in the README index and run its documented command. `make verify` checks the full collection.

The local `make verify` run passed.

## Verification

Local checks passed.

## Limitations

The tools run as independent utilities. Each folder defines its own input contract and exit behavior.
