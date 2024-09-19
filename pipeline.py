def train_and_evaluate(X, y, param_grid):
    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Criar pipeline
    pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(random_state=42))
    ])
    
    # Definir GridSearchCV
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error')
    
    # Treinar o modelo
    grid_search.fit(X_train, y_train)
    
    # Previsão e Avaliação
    y_pred = grid_search.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f'MSE: {mse}, R²: {r2}')
    print(f'Melhores parâmetros: {grid_search.best_params_}')

    return grid_search

# Exemplo de uso
param_grid = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [10, 20],
    'model__min_samples_split': [2, 5]
}

train_and_evaluate(X, y_concentrate, param_grid)
