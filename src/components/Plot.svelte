<script>
  import { merge } from "lodash";

  export let data;
  export let transform = (res) => res;
  export let layout = {};

  let plotElement;

  $: plotElement &&
    data &&
    layout &&
    Plotly.newPlot(
      plotElement,
      transform(data),
      merge(
        {
          margin: {
            l: 50,
            r: 0,
            b: 50,
          },
        },
        layout
      ),
      { responsive: true }
    );
</script>

<div bind:this={plotElement} />
