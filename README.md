# cs3743Project
A repository for uploading updated database files to

# Data sources
- Waypoints derived from the [USPS Facility File](https://postalpro.usps.com/service-hubs-and-facilities/facilityfile)
- Wage data from the U.S. Bureau of Labor Statistics's May 2022 National Industry-Specific Occupational Employment and Wage Estimates for [NAICS 492100 - Couriers and Express Delivery Services](https://www.bls.gov/oes/current/naics4_492100.htm)
    - Except airline pilot wage data -- the BLS does not report hourly wages due to the pay structure of pilots. For the purposes of simplicity, we estimated $33.29 from [ZipRecruiter](https://www.ziprecruiter.com/Salaries/What-Is-the-Average-Commercial-Airline-Pilot-Salary-by-State).

# Acknowledgements
- Container ships are typically measured in TPUs, which are not units of mass -- however, for the purposes of our project, we will treat it as such.