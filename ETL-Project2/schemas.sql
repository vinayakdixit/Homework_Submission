-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/h9cUic
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "diabetes" (
    "pregnancies" INT   NOT NULL,
    "glucose" INT   NOT NULL,
    "blood_pressure" INT   NOT NULL,
    "skin_thickness" INT   NOT NULL,
    "insulin" INT   NOT NULL,
    "bmi" FLOAT   NOT NULL,
    "diabetes_pedigree_function" FLOAT   NOT NULL,
    "age" FLOAT   NOT NULL,
    "outcome" INT   NOT NULL
);

CREATE TABLE "cardio_train" (
    "age" FLOAT   NOT NULL,
    "gender" FLOAT   NOT NULL,
	"height" FLOAT NOT NULL,
    "weight" FLOAT   NOT NULL,
    "ap_hi" INT   NOT NULL,
    "ap_lo" INT   NOT NULL,
    "cholesterol" INT   NOT NULL,
    "glucose" INT   NOT NULL,
    "smoke" INT   NOT NULL,
    "alco" INT   NOT NULL,
    "active" INT   NOT NULL,
    "cardio" INT   NOT NULL,
    "body_mass_index" FLOAT   NOT NULL
);

