<template>
	<div class="">
		<header
			class="sticky top-0 z-10 flex items-center justify-between border-b bg-surface-white px-3 py-2.5 sm:px-5">
			<Breadcrumbs class="h-7" :items="breadcrumbs" />
		</header>
		<div v-if="data.data" class="p-5">
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
				<div class="flex items-center border py-2 px-3 rounded-md text-ink-gray-7">
					<div class="p-2 rounded-md bg-surface-gray-2 mr-3">
						<BookOpen class="w-18 h-18 stroke-1.5" />
					</div>
					<div>
						<div class="text-xl font-semibold mb-1">
							{{ data.data[0].name }}
						</div>
						<div>
							{{ __('Courses') }}
						</div>
					</div>
				</div>
				<div class="flex items-center border py-2 px-3 rounded-md text-ink-gray-7">
					<div class="p-2 rounded-md bg-surface-gray-2 mr-3">
						<LogIn class="w-18 h-18 stroke-1.5" />
					</div>
					<div>
						<div class="text-xl font-semibold mb-1">
							{{ data.data[0].meme_name }}
						</div>
						<div>
							{{ __('Signups') }}
						</div>
					</div>
				</div>
			</div>
			<div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-4">
				<ListView class="h-[150px]" :columns="columns" :rows="data.data" :options="{
					showTooltip: true,
					resizeColumn: true,
				}" row-key="name" />
			</div>
		</div>
	</div>
</template>
<script setup>
import { createResource, createListResource, Breadcrumbs , ListView } from 'frappe-ui'
import { computed, reactive , h , ref , watch } from 'vue'
import { updateDocumentTitle } from '@/utils'
import { formatNumber } from '@/utils'
import { Line, Pie } from 'vue-chartjs'
import {
	Chart as ChartJS,
	Title,
	Tooltip,
	Legend,
	LineElement,
	CategoryScale,
	LinearScale,
	PointElement,
	ArcElement,
	Filler,
} from 'chart.js'

ChartJS.register(
	Title,
	Tooltip,
	Legend,
	LineElement,
	CategoryScale,
	LinearScale,
	PointElement,
	ArcElement,
	Filler
)
import {
	BookOpen,
	LogIn,
} from 'lucide-vue-next'

const columns = [
  {
    label: 'ID',
    key: 'name',
    width: 3,
  },
  {
    label: 'Meme name',
    key: 'meme_name',
    width: 3,
  },
  {
    label: 'description',
    key: 'description',
	width: 3,
  },
  {
    label: 'Score',
    key: 'score',
	width: 2
  },
]


const breadcrumbs = computed(() => {
	return [
		{
			label: 'Testing',
			route: {
				name: 'Testing',
			},
		},
	]
})

const data = createResource({
	url: 'lms.lms.apicustom.get_all',
	auto: true,
})

let htmltesting = createListResource({
	doctype: 'HTMLTesting',
	fields: ['name', 'htmltesting', 'main_content'],
	orderBy: 'creation desc',
	start: 0,
	pageLength: 5,
})

const pageMeta = computed(() => {
	return {
		title: 'Testing',
		description: 'Testing of the platform',
	}
})

updateDocumentTitle(pageMeta)
</script>
