# Cytoflow

This is a fork of [cytoflow/cytoflow](https://github.com/cytoflow/cytoflow). Upstream is tracked as `upstream` remote.

We are working on the library only, not the GUI (cytoflowgui).

Dev environment uses conda (`cf_dev`). See `DEV_SETUP.md` for setup instructions.

## Goal

Improve performance. Key areas:
- Explore migrating from pandas to a faster dataframe library (e.g. polars)
- Speed up file importing and operations
