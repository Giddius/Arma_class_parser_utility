@rem taskarg: ${file}

@Echo off
SETLOCAL EnableDelayedExpansion
set INPATH=%~dp1
set INFILE=%~nx1
set INFILEBASE=%~n1
pushd %INPATH%
set _date=%DATE:/=-%



mkdir "%INPATH%dev_ressources/reports/radon"
radon cc --total-average -s %INFILE% >"%INPATH%dev_ressources/reports/radon/%_date%_%INFILEBASE%_radon_cc_report.txt"

radon mi -s %INFILE% >"%INPATH%dev_ressources/reports/radon/%_date%_%INFILEBASE%_radon_mi_report.txt"

radon raw -s %INFILE% >"%INPATH%dev_ressources/reports/radon/%_date%_%INFILEBASE%_radon_raw_report.txt"

radon hal %INFILE% >"%INPATH%dev_ressources/reports/radon/%_date%_%INFILEBASE%_radon_hal_report.txt"

radon hal -f %INFILE% >"%INPATH%dev_ressources/reports/radon/%_date%_%INFILEBASE%_radon_hal_functions_report.txt"