# BestHacking-League2k23-mISIe1

## Dataset
https://archive.ics.uci.edu/ml/datasets/Online+Retail+II
This Online Retail II data set contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011.The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers.


* Link do Time-Series Split: https://medium.com/@Stan_DS/timeseries-split-with-sklearn-tips-8162c83612b9#:~:text=Time-series%20split%20is%20one,test%20data%20sets%20are%20split.


### Attributes description

* InvoiceNo: Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.
* StockCode: Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.
* Description: Product (item) name. Nominal.
* Quantity: The quantities of each product (item) per transaction. Numeric.
* InvoiceDate: Invice date and time. Numeric. The day and time when a transaction was generated.
* UnitPrice: Unit price. Numeric. Product price per unit in sterling (Â£).
* CustomerID: Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.
* Country: Country name. Nominal. The name of the country where a customer resides.


---

## Notes:
* EDA: wykres krajów (podział na kontynenty), kraj vs cena, produkt vs kraj, 
* Tworzenie nowych kolumn - Customer Country
* Wykrywanie i usuwanie outlierów
* NLP
* Podział Time-Series Split
* Wybór kolumn (!!!)
* Model
* Wizualizacje




## Zrozumienie wybranej bazy danych. (20 pkt)
Przeanalizuj zbiór danych pod kątem rekordów wybrakowanych, korelacji wartości itp. w celu
lepszego zrozumienia wybranych danych oraz możliwie odpowiedniego manipulowania nimi
(feature engineering).
## Wybór i wytrenowanie modelu uczenia maszynowego (40 pkt)
Wybierz algorytm uczenia maszynowego i za jego pomocą stwórz model, który po
wytrenowaniu osiągnie zadowalające metryki. Wyciągnij wnioski na podstawie wyników
uzyskiwanych przez model. Zastanów się, które kolumny mają największy wpływ na
osiągane wyniki, a także postaraj się sformułować jak najdokładniejsze wnioski dotyczące
procesu ich kształtowania.
## Prezentacja, zastosowanie, związek z tematyką (40 pkt)
Wymyśli i zaproponuj w jaki sposób zbudowany model oraz wiedza pozyskana podczas
pracy ze zbiorem danych może zostać zastosowana do rozwiązania jakiegoś problemu w
pracy magazynu. Forma prezentacji jest dowolna, ale będzie również oceniane czy
prezentacja wzbudza ciekawość
