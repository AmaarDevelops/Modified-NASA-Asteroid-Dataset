# 🚀 Near-Earth Asteroids Analysis with Pandas & NumPy

This project explores NASA's Near-Earth Object (NEO) dataset using Python's Pandas and NumPy libraries to analyze asteroid properties, assess hazards, and extract key insights.

---

## 📂 Dataset
- **Source:** NASA/JPL Near-Earth Objects
- **File:** `neo.csv`
- **Attributes Used:**  
  - `name`  
  - `hazardous`  
  - `est_diameter_min`, `est_diameter_max`  
  - `relative_velocity`  
  - `miss_distance`

---

## 🔍 Key Objectives
- Count total asteroids and missing values.
- Separate hazardous vs. non-hazardous asteroids.
- Calculate average diameters.
- Identify fastest and closest asteroids.
- Create a new feature: **Risk Factor** (`High Risk` or `Low Risk`).
- Find top 10:
  - Largest asteroids
  - Fastest asteroids
  - Closest approaches

---

## 📊 Sample Output

Total number of asteroids: 1234
Hazardous: 93
Non-hazardous: 1141
Fastest asteroid: 112,000 km/h (approx)
Closest approach: 1,500,000 km
Top 10 Largest Asteroids:- 
1036 Ganymed (A924 UB)      84.730541
433 Eros (A898 PA)         51.527608
433 Eros (A898 PA)         51.527608
433 Eros (A898 PA)         51.527608
1866 Sisyphus (1972 XA)     19.321462
1866 Sisyphus (1972 XA)      19.321462
4954 Eric (1990 SQ)         18.115068
1627 Ivar (1929 SH)         16.674007
1627 Ivar (1929 SH)         16.674007
2212 Hephaistos (1978 SB)         11.696071

---

## 🧠 What I Learned
- Practical use of `pandas`, `numpy`, and `os.path` for dynamic file loading.
- Logical filtering, sorting, and custom labeling with `np.where()`.
- Created a foundation for future data **visualization** and **machine learning**.

---

## 💡 Next Steps
- [ ] Add data visualizations using **Matplotlib** and **Seaborn**.
- [ ] Use this cleaned dataset to build predictive models in future.

---

## 🧑‍💻 Author

**Amaar Ali**  
Mathematics | Engineering | Hardware | AI/ML Enthusiast  
_"Building the next Apple, one dataset at a time."_
