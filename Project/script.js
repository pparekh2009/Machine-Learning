const models = ['Linear Regression']

const webpagePath = [
    'D://ML/Machine Learning/Machine-Learning/2 Multivariate Regression/Project/templates/index.html'
]

function openPage(modelType) {
    var index = models.indexOf(modelType)

    window.open(webpagePath[index])
}