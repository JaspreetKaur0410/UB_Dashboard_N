query_get_skintype_age = ('''select age_range,
	MAX(CASE WHEN skin_type = 'Dry' THEN people_count_by_skin_type ELSE NULL END) AS 'Dry',
	MAX(CASE WHEN skin_type = 'Oily' THEN people_count_by_skin_type ELSE NULL END) AS 'Oily',
	MAX(CASE WHEN skin_type = 'Sensitive' THEN people_count_by_skin_type ELSE NULL END) AS 'Sensitive',
	MAX(CASE WHEN skin_type = 'Combination' THEN people_count_by_skin_type ELSE NULL END) AS 'Combination'
from(
	select ur.age_range,ur.skin_type,count(skin_type) as 'people_count_by_skin_type'
	from
		(select age, skin_type,
		case when age>=12 and age<=18 then '12-18'
		when age>=19 and age<=25 then '19-25'
		when age>=26 and age<=34 then '26-34'
		when age>=35 and age<=45 then '35-45'
		when age>=46 and age<55 then '46-55'
		else '55+' end as 'age_range'
		from master_recomm) ur
		group by ur.age_range,skin_type
	) temp
group by temp.age_range
order by temp.age_range''')

query_fav_cleanser='''with temp_table as
(
	select ur.age_range, ur.best_match, count(best_match) as 'people_count' 
				from
					(select age,product_type,best_match,
						case when age>=12 and age<=18 then '12-18'
						when age>=19 and age<=25 then '19-25'
						when age>=26 and age<=34 then '26-34'
						when age>=35 and age<=45 then '35-45'
						when age>=46 and age<55 then '46-55'
						else '55+' end as 'age_range'
					from master_recomm where product_type='cleanser'
					) ur
	group by ur.age_range,ur.best_match
)
select * from temp_table where (temp_table.age_range,temp_table.people_count) 
IN (select age_range, max(people_count) 
from temp_table
group by age_range
)'''

query_fav_mosturiser='''with temp_table as
(
	select ur.age_range, ur.best_match, count(best_match) as 'people_count' 
				from
					(select age,product_type,best_match,
						case when age>=12 and age<=18 then '12-18'
						when age>=19 and age<=25 then '19-25'
						when age>=26 and age<=34 then '26-34'
						when age>=35 and age<=45 then '35-45'
						when age>=46 and age<55 then '46-55'
						else '55+' end as 'age_range'
					from master_recomm where product_type='moisturiser'
					) ur
	group by ur.age_range,ur.best_match
)
select * from temp_table where (temp_table.age_range,temp_table.people_count) 
IN (select age_range, max(people_count) 
from temp_table
group by age_range
)'''

query_fav_sunscreen = '''with temp_table as
(
	select ur.age_range, ur.best_match, count(best_match) as 'people_count' 
				from
					(select age,product_type,best_match,
						case when age>=12 and age<=18 then '12-18'
						when age>=19 and age<=25 then '19-25'
						when age>=26 and age<=34 then '26-34'
						when age>=35 and age<=45 then '35-45'
						when age>=46 and age<55 then '46-55'
						else '55+' end as 'age_range'
					from master_recomm where product_type='sunscreen'
					) ur
	group by ur.age_range,ur.best_match
)
select * from temp_table where (age_range,people_count) 
IN (select age_range, max(people_count) 
from temp_table
group by age_range
)'''

query_get_top5_cleanser_count_dry_skin='''select best_match, count(best_match) as count_people_cleanser_dry_skin
from master_recomm
where best_match <>''and product_type='cleanser' and skin_type='dry'
group by best_match
order by count_people_cleanser_dry_skin DESC limit 5'''

query_get_top5_cleanser_count_oily_skin = '''select best_match, count(best_match) as count_people_cleanser_oily_skin
from master_recomm
where best_match <>''and product_type='cleanser' and skin_type='Oily'
group by best_match
order by count_people_cleanser_oily_skin DESC limit 5'''

query_get_top5_cleanser_count_Combination_skin = '''select best_match, count(best_match) as count_people_cleanser_comb_skin
from master_recomm
where best_match <>''and product_type='cleanser' and skin_type='Combination'
group by best_match
order by count_people_cleanser_comb_skin DESC limit 5'''

# AZURE

query_count_products_for_brand='''select brand_name, count(product_name) as total_products_for_brand 
from products 
where brand_name<>'' and brand_name<>'.' and brand_name<>'..'
group by brand_name
having total_products_for_brand>250
order by total_products_for_brand desc'''

query_highest_price_by_brand='''SELECT
    products.brand_name,
    products.product_name,
    REPLACE(products.source_price, ',', '') as highest_price_product
FROM
    products
WHERE   (brand_name, source_price) IN (
        SELECT brand_name, MAX(source_price) 
        FROM products
        GROUP BY brand_name)
AND source_price<>0 AND brand_name<>''
ORDER BY highest_price_product DESC'''

query_people_count_by_brand='''select brand_name,count(user_id) as count_users 
from (select ui.user_name,challenges.* from challenges
	join user_master_data_influencer ui 
	on ui.user_id = challenges.user_id 
	where challenges.brand_name<>''and challenges.brand_name<>'NULL') t
where brand_name<>''
group by brand_name 
having count_users>15
order by count_users DESC'''

query_purchase_count_by_store='''select lower(brand_name) as brandName,shopFrom,count(shopFrom) as count_stores_by_brand 
	from(
	select ui.user_name,challenges.* from challenges
	join user_master_data_influencer ui on ui.user_id = challenges.user_id
	) temp
where brand_name<>''
group by shopFrom,brand_name
having count_stores_by_brand>5
order by count_stores_by_brand DESC'''

query_shopmost_by_brand='''SELECT brandName, shopFrom, MAX(count_stores_by_brand) as highest_purchase_store
FROM (
    SELECT LOWER(brand_name) as brandName, shopFrom, COUNT(shopFrom) as count_stores_by_brand
    FROM (
        SELECT ui.user_name, challenges.*
        FROM challenges
        JOIN user_master_data_influencer ui ON ui.user_id = challenges.user_id
    ) temp
    WHERE brand_name <> ''
    GROUP BY shopFrom, brandName
    ORDER BY count_stores_by_brand DESC
) tt_1
WHERE count_stores_by_brand = (
    SELECT MAX(tt_2.count_stores_by_brand)
    FROM (
        SELECT LOWER(brand_name) as brandName, shopFrom, COUNT(shopFrom) as count_stores_by_brand
        FROM (
            SELECT ui.user_name, challenges.*
            FROM challenges
            JOIN user_master_data_influencer ui ON ui.user_id = challenges.user_id
        ) temp
        WHERE brand_name <> ''
        GROUP BY shopFrom, brandName
        ORDER BY count_stores_by_brand DESC
    ) tt_2
    WHERE tt_1.brandName = tt_2.brandName
)
GROUP BY tt_1.shopFrom, tt_1.brandName
having highest_purchase_store>11
ORDER BY highest_purchase_store DESC;'''

query_recommended_count='''select brandName, 
(CONVERT(GREATEST(count_dermatologist_recommended,count_influencer_recommended,count_social_media_recommended,count_friends_recommended), UNSIGNED INTEGER))
as highest_count,
case  
	GREATEST(count_dermatologist_recommended,count_influencer_recommended,count_social_media_recommended,count_friends_recommended)
    when count_dermatologist_recommended THEN 'Dermatologist'
    when count_influencer_recommended THEN 'Influencer'
    when count_social_media_recommended THEN 'Social-Media'
    when count_friends_recommended THEN 'Friends/Family'
    end as most_recommeded_by
from(
	select replace((lower(brand_name))," ","") as brandName,
	sum(case when recommended_by like '%dermatologist%' then 1 else 0 end) as count_dermatologist_recommended,
	sum(case when recommended_by like '%Influencer%' then 1 else 0 end) as count_influencer_recommended,
	sum(case when recommended_by like '%Social%' then 1 else 0 end) as count_social_media_recommended,
	sum(case when recommended_by like '%Friends%' then 1 else 0 end) as count_friends_recommended
	from(
		select ui.user_name,challenges.* from challenges
		join user_master_data_influencer ui on ui.user_id = challenges.user_id
	) tt_1
	where brand_name<>''
	group by brandName 
	order by count_friends_recommended DESC, count_social_media_recommended DESC, 
	count_influencer_recommended DESC, count_dermatologist_recommended DESC
) t
having highest_count'''

query_most_recommended='''select brand_name, count(recommended_by) as recommendation_count
from(
	select ui.user_name,challenges.* from challenges
	join user_master_data_influencer ui on ui.user_id = challenges.user_id
) t
where brand_name<>''
group by brand_name
having recommendation_count>35
'''

query_socialmedia_influencer_recomm='''select replace((lower(brand_name))," ","") as brandName,
CONVERT( sum(case when recommended_by like '%Influencer%' then 1 else 0 end), UNSIGNED INTEGER) as count_influencer_recommended,
CONVERT( sum(case when recommended_by like '%Social%' then 1 else 0 end),UNSIGNED INTEGER) as count_social_media_recommended
from(
	select ui.user_name,challenges.* from challenges
	join user_master_data_influencer ui on ui.user_id = challenges.user_id
) tt_1
where brand_name<>''
group by brandName 
having count_social_media_recommended>2 and count_influencer_recommended>2
order by count_social_media_recommended DESC, count_influencer_recommended DESC
'''

query_users_data_filters='''select ui.user_name,c.sleepSchedule,ui.age,ui.city,c.sunlightExposure, c.healthIssues, c.stressLevel, c.waterConsumption,
c.exercise, c.medication, c.smoke from challenges c
join user_master_data_influencer ui 
on ui.user_id = c.user_id
where ui.user_name<>'' and ui.age<>'' and ui.city<>'' and c.sleepSchedule<>''and c.sunlightExposure<>'' and  c.healthIssues<>'' and c.stressLevel<>'' and  c.waterConsumption<>'' and 
c.exercise<>'' and c.medication<>'' and c.smoke<>"" '''
