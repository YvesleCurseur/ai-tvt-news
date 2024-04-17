import React from "react";

interface NewsProps {
  data: any[];
}

const News: React.FC<NewsProps> = (props) => {
  const { data } = props;

  /* 
  The reponse from the model is text with * and \n
  So in other to better show the text we need to process it
  */
  function processTranscript(transcript: string) {
    // Split the transcript into categories based on double line breaks
    const categories = transcript.split(/[\n\n]/);

    let htmlOutput = "";
    for (let index = 0; index < categories.length; index++) {
      const category = categories[index];
      // Skip empty categories
      if (!category.trim()) continue;

      // Split the category into lines
      const lines = category.trim().split("\n");

      // Add the first line of the category as a span
      htmlOutput += `<span>${lines[0]}</span>`;

      // Add the remaining lines of the category as spans with a styled dash and line breaks
      for (let lineIndex = 1; lineIndex < lines.length; lineIndex++) {
        htmlOutput += `<span class="styled-dash">${lines[lineIndex]}</span><br/>`;
      }

      // Add a line break between categories
      if (index < categories.length - 1) {
        htmlOutput += "<br/>";
      }
    }

    // Return the processed HTML output
    return htmlOutput;
  }

  return (
    <section id="news" className="fade-in">
      <div className="w-full px-4 mx-auto max-w-7xl md:w-3/4 lg:w-2/4">
        <div className="flex flex-col space-y-12 divide-y divide-white">
          {data.map((item, index) => (
            <div key={index}>
              <div className="pt-12 mb-3 text-sm font-normal text-gray-300 flex justify-between">
                <p>
                  Vidéo Publiée : {new Date(item.published_at).toLocaleString()}
                </p>

                <p>News Créée: {new Date(item.created_at).toLocaleString()}</p>
              </div>
              <h2 className="mb-2 text-xl font-extrabold leading-snug tracking-tight text-gray-100 md:text-3xl">
                <a href="#" className="text-white hover:underline">
                  {item.title}
                </a>
              </h2>
              <p className="mb-4 text-base font-normal text-gray-100 text-justify">
                {React.createElement("div", {
                  dangerouslySetInnerHTML: {
                    __html: processTranscript(item.transcript),
                  },
                })}
              </p>
              {/* Display a YouTube video if the item has a video_id property */}
              {item.video_id && (
                <div className="w-full h-full">
                  <iframe
                    className="mobile-video"
                    src={`https://www.youtube.com/embed/${item.video_id}`}
                    title={item.title}
                    width="640"
                    height="360"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                  ></iframe>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default News;
