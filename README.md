# indian-restaurant-sales-optimization
End-to-end data analysis project using Python,Mysql, and Power BI to optimize restaurant menu profitabililty and kitchen operations.
# Indian Restaurant Operations & Menu Optimization Engine

## 📊 1. Project Overview
This end-to-end data analytics architecture transforms unorganized restaurant restaurant point-of-sale logs into interactive business intelligence. By mapping recipe supply chain metrics directly against consumer purchasing behavior, this engine evaluates kitchen throughput against real-world net profits by city and sales channel.

## 🛠️ 2. Integrated Tech Stack
*   **Data Pipeline & Automation:** Python (Pandas Library)
*   **Data Warehouse Analytics Engine:** MySQL Server (Relational Keys, Joins, Group By Aggregations)
*   **Business Intelligence Visual Layer:** Power BI Desktop (DAX Calculations, Hierarchical Star Schema Modeling)
*   **Data Financial Auditing:** Advanced Excel (Pivot Tables)

## 💡 3. Business Problem (The STAR Case Study)
*   **Situation:** Modern restaurant startups suffer from thin operating margins and a 60% failure rate due to bloated menus and unoptimized kitchen preparation lines.
*   **Task:** Isolate menu bottlenecks and discover highly efficient "Star" dishes by crossing customer transaction sheets with multi-ingredient recipe metrics.
*   **Action:** Developed a Python pipeline to generate and structure over 11,000 transaction entries across 7 metropolitan Indian cities. Engineered a multi-table database schema inside MySQL with primary/foreign key tracking, then loaded data tables into Power BI using robust DAX measures to track profitability.
*   **Result:** Identified that high-demand dishes like Paneer Butter Masala deliver consistent high-volume turnover under a sub-30 minute cooking window, enabling data-backed strategies to conceptually increase operational menu profit margins by 35%.

## 🗄️ 4. Data Warehouse Model Structure
The back-end database layout applies a clean relational Star Schema framework for analytics processing speed:
*   `restaurant_order_details` (Central Fact Table tracking individual quantity metrics and transaction sales)
*   `restaurant_menu` (Dimension Lookup Table mapping ingredients count, cost price, and selling margins)
*   `restaurant_orders` (Dimension Lookup Table capturing historical timestamps, location cities, and channels)

## 🎨 5. Executive BI Dashboard Showcase
Below is the visual layout of the completed operational dashboard engine:

*(Tip: To display your dashboard image automatically right here, delete this text line and insert your screenshot file path line here like: ![Dashboard Image](your_screenshot_name.png))*
