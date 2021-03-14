import { writable } from "svelte/store";

export let job = writable("warrior");
export let level = writable(140);
export let hp = writable(30000);
export let avoid = writable(45);
export let wdef = writable(100);
export let mdef = writable(100);
export let str = writable(600);
export let dex = writable(40);
export let luk = writable(4);
export let int = writable(4);
