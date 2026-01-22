import pandas as pd

class RetailAnalytics:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.raw_data = []

    def run_assessment(self, emails: list):
        self.raw_data = [] # Reset pour chaque nouveau calcul
        for text in emails:
            try:
                result = self.analyzer.process_email(text)
                self.raw_data.append(result.model_dump())
            except Exception as e:
                print(f"Saut d'un email suite à une erreur : {e}")
        
        return self._generate_report()

    def _generate_report(self):
        if not self.raw_data:
            return "Aucune donnée n'a pu être analysée."
            
        df = pd.DataFrame(self.raw_data)
        neg_df = df[df['sentiment'] == 'Negative']
        
        if neg_df.empty:
            return "Aucun sentiment négatif détecté dans ces emails."

        top_neg_category = neg_df['product_category'].value_counts().idxmax()
        top_complaint_store = neg_df['store_location'].value_counts().idxmax()
        
        return {
            "critical_category": top_neg_category,
            "worst_store": top_complaint_store,
            "total_processed": len(df)
        }