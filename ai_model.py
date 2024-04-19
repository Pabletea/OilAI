import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import source_manager
def aiModel():
    # Load the CSV file into a pandas DataFrame
    
    data = pd.read_csv(source_manager.sourceConverter)

    # Select the relevant columns for training
    features = data[["Fecha:", "Precio gasolina 95 E5", "Precio gasolina 95 E10", "Precio gasolina 95 E5 Premium", "Precio gasolina 98 E5", "Precio gasolina 98 E10", "Precio gasóleo A", "Precio gasóleo Premium", "Precio gasóleo B", "Precio gasóleo C", "Precio bioetanol", "% bioalcohol", "Precio biodiésel", "% éster metílico", "Precio gases licuados del petróleo", "Precio gas natural comprimido", "Precio gas natural licuado", "Precio hidrógeno"]]

    # Remove rows with missing values
    features = features.dropna()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features.drop("Fecha:", axis=1), features["Fecha:"], test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Calculate the root mean squared error
    rmse = mean_squared_error(y_test, predictions, squared=False)
    print("Root Mean Squared Error: ", rmse)

    # Predict the price for the next day
    next_day_data = data.iloc[-1, 1:].values.reshape(1, -1)
    next_day_price = model.predict(next_day_data)
    print("Predicted price for the next day: ", next_day_price)