CREATE VIEW bmi_view AS
SELECT c.body_mass_index, c.cardio, d.outcome FROM cardio_train c, diabetes d
WHERE c.body_mass_index = d.bmi;

CREATE VIEW age_view AS
SELECT c.age, c.cardio, d.outcome FROM cardio_train c, diabetes d
WHERE c.age = d.age;

CREATE VIEW age_bmi_combo AS
SELECT c.age, c.cardio, c.body_mass_index, d.bmi, d.outcome FROM cardio_train c, diabetes d
WHERE c.age = d.age;
