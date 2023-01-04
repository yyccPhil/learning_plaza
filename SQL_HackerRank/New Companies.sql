/*
It successfully evoked the memory of thousands of lines of a query when I was a DA intern in Maimai (Chinese version of LinkedIn), lol.
*/
select company_code, founder, le_cnt, se_cnt, ma_cnt, em_cnt
from company
left join (
    select company_code, count(distinct lead_manager_code) as le_cnt, se_cnt, ma_cnt, em_cnt
    from lead_manager
    left join (
        select company_code, count(distinct senior_manager_code) as se_cnt, ma_cnt, em_cnt
        from senior_manager
        left join (
            select company_code, em_cnt, count(distinct manager_code) as ma_cnt
            from manager
            left join (
                select company_code, count(distinct employee_code) as em_cnt
                from employee
                group by company_code) t_em using(company_code)
            group by company_code, em_cnt) t_ma using(company_code)
        group by company_code, ma_cnt, em_cnt) t_se using(company_code)
    group by company_code, se_cnt, ma_cnt, em_cnt) t_le using(company_code)
-- order by CAST(SUBSTR(company_code, 2, LENGTH(company_code)-1) AS UNSIGNED)
order by company_code
