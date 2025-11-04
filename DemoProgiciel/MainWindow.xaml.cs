using System.Windows;

namespace DemoApp
{
    public partial class MainWindow : Window
    {
        private int compteurClics = 0;

        public MainWindow()
        {
            InitializeComponent();
            AfficherMessageBienvenue();
        }

        private void AfficherMessageBienvenue()
        {
            ResultatTextBlock.Text = "Bienvenue dans l'application de démonstration!\n\n" +
                                    "Cette application WPF .NET 8 est conçue pour tester " +
                                    "le déploiement avec InnoSetup.\n\n" +
                                    "Entrez votre nom ci-dessus et cliquez sur 'Saluer' pour commencer.";
        }

        private void SaluerButton_Click(object sender, RoutedEventArgs e)
        {
            compteurClics++;
            
            string nom = NomTextBox.Text.Trim();
            
            if (string.IsNullOrEmpty(nom))
            {
                ResultatTextBlock.Text = "⚠️ Veuillez entrer un nom avant de saluer!";
                return;
            }

            string message = $"👋 Bonjour {nom}!\n\n" +
                           $"Ceci est votre visite numéro {compteurClics}.\n\n" +
                           $"📅 Date et heure: {DateTime.Now:dddd d MMMM yyyy, HH:mm:ss}\n" +
                           $"💻 Système: {Environment.OSVersion}\n" +
                           $"🖥️ Machine: {Environment.MachineName}\n" +
                           $"👤 Utilisateur: {Environment.UserName}\n\n" +
                           "Cette application démontre:\n" +
                           "• Interface WPF moderne avec .NET 8\n" +
                           "• Gestion d'événements et état de l'application\n" +
                           "• Affichage d'informations système\n" +
                           "• Prête pour le déploiement avec InnoSetup";

            ResultatTextBlock.Text = message;
        }
    }
}
