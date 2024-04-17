import Header from "@/components/Header";
import Footer from "@/components/Footer";

const About = () => {
  return (
    <div>
      <div className="mb-12">
        <Header />
      </div>

      <div className="max-w-screen-md mx-auto">
        <h1 className="text-3xl font-bold mb-8 text-center">
          À Propos + Disclaimer
        </h1>
        <h2 className="text-2xl font-bold mb-4">Problème</h2>
        <p className="text-justify mb-6">
          En tant qu'auditeur fidèle de la chaîne YouTube togolaise (TVT), je me
          suis souvent retrouvé à vouloir rester informé même lorsque mon emploi
          du temps était serré. Il y a eu de nombreuses fois où je n'ai pas pu
          regarder toutes les actualités de la TVT, et cela m'a laissé avec un
          sentiment de frustration de ne pas être pleinement informé. C'est de
          là qu'est née l'idée de cet petit projet.
        </p>
        <h2 className="text-2xl font-bold mb-4">Solution</h2>
        <p className="text-justify mb-6">
          Mon objectif est simple : me permettre à de rester informé, même
          lorsque je manque de temps. Pour ca je m'offre un accès rapide et
          facile aux résumés des actualités de la chaîne YouTube togolaise
          (TVT), me garantissant ainsi de ne manquez aucune information
          importante.
        </p>
        <h2 className="text-2xl font-bold mb-4">Fonctionnalités</h2>
        <ul className="list-disc pl-6 mb-6">
          <li className="text-justify mb-2">
            Des résumés rapides et accessibles de toutes les informations
            abordées dans les vidéos de la TVT.
          </li>
          <li className="text-justify mb-2">
            La possibilité de rester au fait de l'actualité, même en déplacement
            ou pendant les journées les plus mouvementées.
          </li>
        </ul>
        <h2 className="text-2xl font-bold mb-4">Technologies Utilisées</h2>
        <p className="text-justify mb-6">
          Pour concevoir ce projet j'ai utilisé :
        </p>
        <ul className="list-disc pl-6 mb-6">
          <li className="text-justify mb-2">
            L'Intelligence Artificielle, notamment le modèle GPT-3.5 de OpenAI,
            génère des résumés intelligents et précis des Actualités de la
            chaîne YouTube togolaise (TVT).
          </li>
          <li className="text-justify mb-2">
            L'API de YouTube est intégrée pour accéder aux vidéos de la chaîne
            et les transcrire quotidiennement, facilitant ainsi la génération
            des résumés écrits.
          </li>
        </ul>
        <h2 className="text-2xl font-bold mb-4">Ce que J'ai Appris</h2>
        <p className="text-justify mb-6">
          Le développement d'une solution utilisant l'IA a été une aventure
          compliquée mais enrichissante. (Je ne l'avais encore jamais fait)
          <br />
          Ce projet m'a permis de découvrir les possibilités offertes par
          l'intelligence artificielle dans le domaine de la rédaction
          automatique. On pourrait penser plus tard comme perspective à envoyer
          les informations sous forme de Newsletter ou même à créer un article
          pour chaque vidéo publiée dans le but d'alimenter un blog pour les
          lecteurs.
          <br />
          J'ai également développé une expertise approfondie dans l'utilisation
          de technologies modernes telles que Next.js, TypeScript et FastAPI.
        </p>
        <h2 className="text-2xl font-bold mb-4 text-center"> Disclaimer </h2>
        <p className="text-justify mb-10">
          Ce projet est une application développée de manière indépendante et
          n'est en aucun cas affiliée à la chaîne YouTube togolaise (TVT) ou à
          ses propriétaires. Les informations fournies sont des résumés et des
          reformulations générés automatiquement à partir du contenu disponible
          publiquement sur la chaîne YouTube, et ne sont pas garanties pour être
          complètes, précises ou à jour. Je décline toute responsabilité quant à
          l'utilisation des informations fournies par l'application et
          recommande aux utilisateurs de vérifier les sources originales pour
          toute information critique ou urgente.
        </p>
      </div>

      <div>
        <Footer />
      </div>
    </div>
  );
};

export default About;
