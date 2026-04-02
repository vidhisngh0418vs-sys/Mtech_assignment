def pipeline():
    logging.info("Pipeline started")

    df = preprocess()
    logging.info("Preprocessing complete")

    df = feature_engineering(df)
    logging.info("Feature engineering complete")

    run_eda(df)
    logging.info("EDA complete")
