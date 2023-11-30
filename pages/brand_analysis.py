from query import *
from main import *
# st.set_page_config(page_title="UB-Beauty", layout='wide')
# ----------------------------------- brands-analysis --------------------------------------- #
def convert_to_pd(query_var):
    return pd.DataFrame(query_var)

# start - USER DATA
df_data_users=convert_to_pd(get_users_data_filters())
# st.dataframe(df_data_users)
# end - USER DATA

# start - Brands Used by customers - recommended by Social-Media & Influencers
st.info('Top Brands Used by customers - recommended by Social-Media & Influencers')
df_socialmedia_influencer_recomm=convert_to_pd(get_socialmedia_influencer_recomm())
st.dataframe(df_socialmedia_influencer_recomm)

base_chart = alt.Chart(df_socialmedia_influencer_recomm).mark_bar().encode(
            y = alt.Y("brandName")
        ).properties(
            width=300,
            height=200
        )
print(df_socialmedia_influencer_recomm['count_influencer_recommended'])
base_chart.encode(x=alt.X('count_influencer_recommended')) | base_chart.encode(x=alt.X('count_social_media_recommended'))
# st.altair_chart(base_chart)
# end - Brands Used by customers - recommended by Social-Media & Influencers

# start - highest-price-product for different brands
df_get_highest_price_by_brand=convert_to_pd(get_highest_price_by_brand())
# st.info('HIGHEST_PRICE_PRODUCT BY BRAND')
# st.dataframe(df_get_highest_price_by_brand)
# end - highest-price-product for different brands

# start - how many people using different brands
st.info('Top 20 brands - used by people')
df_people_count_by_brand=convert_to_pd(get_people_count_by_brand())
chart_count_people_by_brand=alt.Chart(df_people_count_by_brand).mark_bar(size=4).encode(
        x='count_users',
        y='brand_name',
        color='count_users'
        ).properties(width = 1800, height = 500)
st.altair_chart(chart_count_people_by_brand, use_container_width=True)
# end - how many people using different brands

# start - Number of products for brands
get_count_products_by_brand=get_count_products_for_brand()
df_get_count_prodcutts_by_brand=pd.DataFrame(get_count_products_by_brand)
st.info('Top Brands based on highest number of products in the market')
chart_count_products_by_brand=alt.Chart(df_get_count_prodcutts_by_brand).mark_bar(size=4).encode(
        x='total_products_for_brand',
        y='brand_name',
        color='total_products_for_brand'
        ).properties(width = 1900, height = 300)
st.altair_chart(chart_count_products_by_brand, use_container_width=True)
# end - Number of products for brands

# start - How many purchases from each brand from different stores
st.info('Number of Purchases for different brands from different stores - Amazon has more hold than Nykaa & Local-Stores')
df_purchase_count_by_store=convert_to_pd(get_purchase_count_by_store())
chart_purchase_count_by_store=alt.Chart(df_purchase_count_by_store).mark_bar(size=20).mark_bar(size=6).encode(
        x='brandName',
        y='count_stores_by_brand',
        color='shopFrom').properties(width = 1150, height = 500)
st.altair_chart(chart_purchase_count_by_store)
# end - How many purchases from each brand from different stores

# start - where people shop the most for my brand
st.info('Highest-Purchased-Store for different brands - Amazon is the highest purchased store')
df_shopmost_by_brand=convert_to_pd(get_shopmost_by_brand())
chart_shopmost_by_brand=alt.Chart(df_shopmost_by_brand).mark_bar(size=6).encode(
        x='brandName',
        y='highest_purchase_store',
        color='shopFrom').properties(width = 1150, height = 500)
st.altair_chart(chart_shopmost_by_brand)
# end - where people shop the most for my brand

# start - How many people for each "recommended_by" recommeded the brand 
st.info('Top 10 MOST RECOMMENDED BRANDS')
df_recommended_count=convert_to_pd(get_most_recommended())
chart_recommended_count=alt.Chart(df_recommended_count).mark_bar(size=6).encode(
        x='recommendation_count',
        y='brand_name').properties(width = 1150, height = 400)
st.altair_chart(chart_recommended_count)
# end - How many people for each "recommended_by" recommeded the brand 







            
    
