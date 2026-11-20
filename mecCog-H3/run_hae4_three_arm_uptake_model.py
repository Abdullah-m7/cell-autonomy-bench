#!/usr/bin/env python3
"""Posthoc HAE-4 3-arm model adequacy, not mechanism identification or source p-value."""
from pathlib import Path
import json,datetime,statistics,math,hashlib
B=Path(__file__).resolve().parent
src=B/"Xia2024_Fig7_HAE4_Immunodepletion_Audit_20261121.json"
x=json.loads(src.read_text())
assert x["source_sha256"]=="47d9439f523f58c2e075e0dd853220da9b7971fa3541cfc675913c88db86617e"
tests=[]
for model,group in x["groups"].items():
    U=group["uptake"]
    Uis=U["isotype_mean"]
    Uip=U["HAE4_mean"]
    Uorig=U["unprocessed_mean"]
    assert Uis>Uip>=0 and Uorig>0
    for marker,item in group.items():
        if marker=="uptake":continue
        Yis=item["isotype_mean"]
        Yip=item["HAE4_mean"]
        Yor=item["unprocessed_mean"]
        b=(Yis-Yip)/(Uis-Uip)
        a=Yis-b*Uis
        pred=a+b*Uorig
        residual=Yor-pred
        true_sd=statistics.stdev(item["unprocessed_Aβ_APOE4_original_three"])
        true_cv=true_sd/Yor
        error=abs(residual)/Yor
        test={"cell":model,"marker":marker,
          "source_mean_uptake":{"original":Uorig,"isotype":Uis,"HAE4":Uip},
          "source_mean_cytokine_pg_ml":{"original":Yor,"isotype":Yis,"HAE4":Yip},
          "fit_two_point_linear_affine_intercept":a,
          "fit_two_point_slope_pgml_per_uptake_unit":b,
          "fit_predicted_unprocessed_cytokine_pgml":pred,
          "observed_minus_predicted_unprocessed_pgml":residual,
          "absolute_relative_prediction_error":error,
          "within_unprocessed_culture_SD_pgml":true_sd,
          "within_unprocessed_culture_CV":true_cv,
          "abs_prediction_error_within_1_SD_of_unprocessed_replicates":abs(residual)<=true_sd,
          "slope_nonnegative":b>=0,
          "intercept_nonnegative":a>=0}
        tests.append(test)
        print("MODEL3",model,marker,"slope",round(b,3),"intercept",round(a,3),
              "Yorig_prediction",round(pred,3),"Yorig_observed",round(Yor,3),
              "error_pct",round(error*100,2),"observed_CV_pct",round(true_cv*100,2),
              "error_lt_source_SD",test["abs_prediction_error_within_1_SD_of_unprocessed_replicates"],flush=True)
assert len(tests)==8
summary={"n_endpoints":len(tests),
 "n_predictions_within_1_source_original_arm_culture_SD":sum(x["abs_prediction_error_within_1_SD_of_unprocessed_replicates"] for x in tests),
 "n_nonnegative_slopes":sum(x["slope_nonnegative"] for x in tests),
 "n_nonnegative_intercepts":sum(x["intercept_nonnegative"] for x in tests),
 "median_absolute_relative_error":statistics.median(x["absolute_relative_prediction_error"] for x in tests),
 "max_absolute_relative_error":max(x["absolute_relative_prediction_error"] for x in tests)}
print("SUMMARY",summary,flush=True)
out={"status":"POSTHOC_THREE_ARM_GROUP_MEAN_AFFINE_MODEL_CONSISTENCY_CHECK",
 "study":"Xia et al Nat Commun 2024 DOI 10.1038/s41467-024-49028-z Fig7C-L",
 "source_fig7_result_file_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
 "utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "model":"Y=a+b*U fit to isotype vs HAE-4 group means; predict original unprocessed stimulus mean",
 "measurements":tests,"summary":summary,
 "limitations":[
  "Mathematical descriptive calibration: two treatment arms determine both parameters exactly, leaving only one third-arm mean for an informal residual check.",
  "Uptake fluorescence and cytokine ELISA measured separately; no paired culture-level covariance or mediation estimate possible.",
  "Source antibody depletion changes extracellular ligand amount and molecular composition; the exclusion restriction for uptake-mediated causal identification is violated.",
  "The modeled intercept is a mathematical extrapolation and is not measured zero-stimulus cytokine baseline.",
  "Neither a small model error nor eight correlated cases identifies a unique biological mechanism. The source authors published these outcomes in 2024.",
  "A positive b within ApoE4 immunodepletion DOES NOT imply that across ApoE3 vs ApoE4, inflammation is a monotone function of uptake under chemically different ligands."
 ]}
dst=B/"Xia2024_HAE4_ThreeArm_UptakeOnly_Model_Check_20261121.json"
dst.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
print("SAVE",dst,flush=True)
